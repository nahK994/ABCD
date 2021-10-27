import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginService } from '../login/login.service';
import { Teacher } from './teacher.model'

@Injectable({
  providedIn: 'root'
})
export class TeacherService {

  baseUrl_Get: string = 'http://localhost:8001/teacher/';
  baseUrl_Create: string = 'http://localhost:8000/teacher/create/';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': 'Bearer '+localStorage.getItem(this._logInService.accessToken)})
  };

  constructor(
    private http: HttpClient,
    private _logInService: LoginService,
  ) { }

  getTeacher(teacherId: string) {
    let url = this.baseUrl_Get+teacherId;
    console.log("FUN ===> ", this.httpOptions.headers)
    return this.http.get<Teacher[]>(url, this.httpOptions);
  }

  createTeacher(teacherInfo: TeacherPayload) {
    return this.http.post<TeacherPayload>(this.baseUrl_Create, teacherInfo, this.httpOptions);
  }
}

export interface TeacherPayload {
  userId: string;
  name: string;
  orgName: string;
  aboutMe: string;
  email: string;
  password: string;
}