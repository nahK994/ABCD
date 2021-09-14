import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Teacher } from './teacher.model'

@Injectable({
  providedIn: 'root'
})
export class TeacherService {

  baseUrl_Get: string = 'http://localhost:8001/teacher/';
  baseUrl_Post: string = 'http://localhost:8000/teacher/';
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient
  ) { }

  getTeacher(teacherId: string) {
    let url = this.baseUrl_Get+teacherId
    return this.http.get<Teacher[]>(url);
  }

  postTeacher(teacherInfo: TeacherPayload) {
    return this.http.post<TeacherPayload>(this.baseUrl_Post, teacherInfo, this.httpOptions);
  }
}

export interface TeacherPayload {
  teacherId: string;
  userName: string;
  email: string;
  password: string;
}