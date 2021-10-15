import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  baseUrl_Login: string = 'http://localhost:8000/login/';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient
  ) { }
  
  createUser(payload: UserPayload) {
    return this.http.post<UserPayload>(this.baseUrl_Login, payload, this.httpOptions);
  }
}

interface UserPayload
{
  email: string;
  password: string;
}
