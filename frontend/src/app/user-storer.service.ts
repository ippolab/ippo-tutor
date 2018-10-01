import { Injectable } from '@angular/core';

import { User } from './users';
import { HttpclientService } from './httpclient.service';

@Injectable()
export class UserStorerService {

  private currentUser: User;

  constructor(private httpClient: HttpclientService) {
    this.currentUser = new User('', '', false);
   }

  setUser(user: User): void {
    this.currentUser = user;
    this.saveUserIntoStorage();
  }

  getUser(): User {
    return this.currentUser;
  }

  saveUserIntoStorage(): void {
    localStorage.setItem('ippouserusername', this.currentUser.username);
    localStorage.setItem('ippousertoken', this.currentUser.token);
    localStorage.setItem('ippoisstudent', `${this.currentUser.istutor}`);
  }

  loadUserFromStorage() {
    const username = localStorage.getItem('ippouserusername');
    const token = localStorage.getItem('ippousertoken');
    const isstudent = localStorage.getItem('ippoisstudent');

    this.currentUser.username = username;
    this.currentUser.token = token;
    this.currentUser.istutor = Boolean(isstudent);

    this.httpClient.tryLoginWithToken(username, token).subscribe((data: User) => {
      this.currentUser.username = username;
      this.currentUser.token = token;
      this.currentUser.istutor = data.istutor;

      this.saveUserIntoStorage();
    }, error => {
      this.currentUser = new User('', '', false);
      console.log(error['message']);
    });
  }
}
