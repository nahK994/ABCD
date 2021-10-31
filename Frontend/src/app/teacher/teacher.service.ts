import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AppService } from '../app.service';
import { LoginResponse, LoginService } from '../login/login.service';
import { Teacher } from './teacher.model'

@Injectable({
  providedIn: 'root'
})
export class TeacherService {

  baseUrl_Get: string = 'http://localhost:8001/teacher/';
  baseUrl_Create: string = 'http://localhost:8000/teacher/create/';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json'})
  };

  constructor(
    private http: HttpClient,
    private _appService: AppService,
    private _loginService: LoginService
  ) { }

  getTeacher(teacherId: string) {
    let url = this.baseUrl_Get+teacherId;
    const headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Authorization', 'Bearer '+localStorage.getItem(this._appService.accessToken));
    this.httpOptions = {
      headers: headers
    }
    return this.http.get<Teacher[]>(url, this.httpOptions);
  }

  async createTeacher(teacherInfo: TeacherPayload) {
    let response: LoginResponse = await this.http.post<LoginResponse>(this.baseUrl_Create, teacherInfo, this.httpOptions).toPromise();
    this._loginService.setLoginInformation(response);
    return response.userId;
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