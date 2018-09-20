import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { User } from './users'
import { Observable } from 'rxjs';
import { Student } from './users';


@Injectable({
  providedIn: 'root'
})
export class HttpclientService {

  constructor(
    private http: HttpClient) { }

  sendAuthForm(username:string, password:string) : Observable<User>{
    return this.http.post<User>('servername/api/users/login/', {'username': username, 'password': password})
  }

  getStudent():Observable<Student>{
    return this.http.get<Student>('servername/api/students/studentname/');
  }

}
