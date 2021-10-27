import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { LoginService } from "../login/login.service";


@Injectable()
export class AccessTokenInterceptor implements HttpInterceptor {

    constructor(
        private _loginService: LoginService
    ) { }

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        if (this._loginService.getAccessToken) {
            return next.handle(this.getTokenizedRequest(request));
        }

        return next.handle(request);

    }

    private getTokenizedRequest(request: HttpRequest<any>): HttpRequest<any> {
        let tokenizedRequest = request;
        const token = this._loginService.getAccessToken;
        if (token) {
            const tokenValue = 'Bearer ' + token;
            tokenizedRequest = request.clone({ setHeaders: { Authorization: tokenValue } });
        }
        return tokenizedRequest;
    }
}