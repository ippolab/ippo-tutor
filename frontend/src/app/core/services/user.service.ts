import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable ,  BehaviorSubject ,  ReplaySubject } from 'rxjs';

import { ApiService } from './api.service';
import { JwtService } from './jwt.service';
import { User } from '../models';
import { map ,  distinctUntilChanged } from 'rxjs/operators';
import { pipe } from '@angular/core/src/render3/pipe';


@Injectable()
export class UserService {
  private currentUserSubject = new BehaviorSubject<User>({} as User);
  public currentUser = this.currentUserSubject.asObservable().pipe(distinctUntilChanged());

  private isAuthenticatedSubject = new ReplaySubject<boolean>(1);
  public isAuthenticated = this.isAuthenticatedSubject.asObservable();

  private isTutorSubject = new ReplaySubject<boolean>(1);
  public isTutor = this.isTutorSubject.asObservable();

  constructor (
    private apiService: ApiService,
    private http: HttpClient,
    private jwtService: JwtService
  ) {}

  populate() {
    if (this.jwtService.getToken()) {
      this.apiService.get('/users/check-auth/')
      .subscribe(
        data => this.setAuth(data),
        err => this.purgeAuth()
      );
    } else {
      this.purgeAuth();
    }
  }

  setAuth(user: User) {
    this.jwtService.saveToken(user.token);
    this.currentUserSubject.next(user);
    this.isAuthenticatedSubject.next(true);
    this.isTutorSubject.next(user.is_tutor);
  }

  purgeAuth() {
    this.jwtService.destroyToken();
    this.currentUserSubject.next({} as User);
    this.isAuthenticatedSubject.next(false);
    this.isTutorSubject.next(false);
  }

  attemptAuth(credentials): Observable<User> {
    return this.apiService.post('/users/login/', credentials)
      .pipe(map(
      data => {
        let user = {
          token: data['token'],
          is_tutor: data['user']['is_tutor'],
          username: data['user']['username']
        }
        this.setAuth(user);
        return data;
      }
    ));
  }

  getCurrentUser(): User {
    return this.currentUserSubject.value;
  }

  changePassword(username, password_credentials): Observable<User> {
    return this.apiService
    .put(`/users/${username}`, { password_credentials });
  }

}
