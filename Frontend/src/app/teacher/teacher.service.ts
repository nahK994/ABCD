import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Teacher } from './teacher.model'

@Injectable({
  providedIn: 'root'
})
export class TeacherService {

  baseUrl: string = 'http://localhost:8001/teacher/';
  constructor(
    private http: HttpClient
  ) { }

  getTeacher(teacherId: string) {
    let url = this.baseUrl+teacherId
    console.log("HiHi ==> ", url)
    return this.http.get<Teacher[]>(url);
  }
}
