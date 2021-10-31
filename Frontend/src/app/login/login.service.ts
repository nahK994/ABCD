import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { AppService } from '../app.service';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  baseUrl_Login: string = 'http://localhost:8000/login/';
  baseUrl_Logout: string = 'http://localhost:8000/logout/';
  userId: string;

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
    private _appService: AppService
  ) { }
  
  async loginUser(payload: LoginPayload) {
    let response = await this.http.post<LoginResponse>(this.baseUrl_Login, payload, this.httpOptions).toPromise();
    this.setLoginInformation(response);

    return this.userId;
  }

  setLoginInformation(response) {
    this._appService.setAssets(response.refreshToken, response.accessToken);
    this.userId = response.userId;
  }

  async logoutUser() {
    await this.http.post<LoginResponse>(this.baseUrl_Logout, localStorage.getItem(this._appService.refreshToken), this.httpOptions).toPromise();
    this._appService.removeAssets();
    this.userId = null;
  }

  get getAccessToken() {
    return localStorage.getItem(this._appService.accessToken);
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
