import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  readonly accessToken = "JWT_TOKEN";
  readonly refreshToken = "REFRESH_TOKEN";
  baseUrl_RefreshAccessToken: string = 'http://localhost:8000/refresh-access-token/';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient
  ) { }

  async refreshAccessToken(): Promise<void> {
    let response = await this.http.post<Assets>(this.baseUrl_RefreshAccessToken, localStorage.getItem(this.refreshToken), this.httpOptions).toPromise();
    this.setAssets(response.refreshToken, response.accessToken);
  }

  setAssets(refreshToken, accessToken) {
    this.removeAssets();
    localStorage.setItem(this.refreshToken, refreshToken);
    localStorage.setItem(this.accessToken, accessToken);
  }

  removeAssets() {
    localStorage.removeItem(this.refreshToken);
    localStorage.removeItem(this.accessToken);
  }
}

interface Assets {
  accessToken: string;
  refreshToken: string;
}
