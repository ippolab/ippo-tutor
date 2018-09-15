import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {HttpModule} from '@angular/http';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class WebserviceService {

  serverUrl: String = "localhost";

  constructor(private http: HttpClient) {
  };
  login(username: string, password:string):Observable<String> {
  return this.http.post(this.serverUrl, {username, password});
  }

}
