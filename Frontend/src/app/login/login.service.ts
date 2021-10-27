import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  baseUrl_Login: string = 'http://localhost:8000/login/';
  baseUrl_Logout: string = 'http://localhost:8000/logout/';
  readonly accessToken = "JWT_TOKEN";
  readonly refreshToken = "REFRESH_TOKEN";
  userId: string;

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient
  ) { }
  
  async loginUser(payload: LoginPayload) {
    let response = await this.http.post<LoginResponse>(this.baseUrl_Login, payload, this.httpOptions).toPromise();
    this.setAssets(response.refreshToken, response.accessToken, response.userId);
    return this.userId;
  }

  async logoutUser() {
    let payload: LogoutPayload = {
      refreshToken: localStorage.getItem(this.refreshToken)
    }
    await this.http.post<LoginResponse>(this.baseUrl_Logout, payload).toPromise();
    this.removeAssets();
  }

  setAssets(refreshToken, accessToken, userId) {
    localStorage.setItem(this.refreshToken, refreshToken);
    localStorage.setItem(this.accessToken, accessToken)
    this.userId = userId
  }

  removeAssets() {
    localStorage.removeItem(this.refreshToken);
    localStorage.removeItem(this.accessToken)
    this.userId = null;
  }

  get getAccessToken() {
    return localStorage.getItem(this.accessToken);
  }
}

export interface LoginResponse
{
  userId: string;
  accessToken: string;
  refreshToken: string;
}

interface LoginPayload
{
  email: string;
  password: string;
}

interface LogoutPayload
{
  refreshToken: string;
}
