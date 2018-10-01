import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { User } from './users';
import { Observable } from 'rxjs';
import { Student } from './users';

import { environment } from '../environments/environment';


@Injectable()
export class HttpclientService {

  private serverUrl: string;
  private errorMessage: string;

  constructor(private http: HttpClient) {
    this.serverUrl = environment.serverUrl;
  }

  public get error(): string {
    return this.errorMessage;
  }

  private addAuthorizationHeader(headers: HttpHeaders, token: string): void {
    headers.append('Authorization', `JWT ${token}`);
  }

  login(username: string, password: string): Observable<any> {
    return this.http.post(`${this.serverUrl}/api/users/login/`, { 'username': username, 'password': password });
  }

  getStudent(): Observable<Student> {
    return this.http.get<Student>('servername/api/students/studentname/');
  }

  tryLoginWithToken(username: string, token: string): Observable<any> {
    const options = {
      headers: new HttpHeaders({
        'Authorization': `JWT ${token}`
      })
    };

    return this.http.get(`${this.serverUrl}/api/users/${username}/`, options);
  }
}
