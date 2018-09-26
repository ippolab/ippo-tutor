import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';


import { User } from '../users';
import { HttpclientService } from '../httpclient.service';
import { Student } from '../users';
import { UserStorerService } from '../user-storer.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
  providers: []
})

export class AuthComponent implements OnInit {
  username = '';
  password = '';
  error = false;
  errorMessage = '';

  constructor(private clientService: HttpclientService,
    private storageService: UserStorerService,
    private router: Router) {
    if (storageService.loadUserFromStorage()) {
      router.navigate(['/']);
    }
  }

  onClickLogin(username: string, password: string) {
    const user = new User('', '', false);
    this.clientService.login(username, password).subscribe(
      (data) => {
        user.token = data['token'];
        user.username = data['user']['username'];
        user.istutor = data['user']['is_tutor'];

        if (user.istutor) {
          // TODO
        }

        this.storageService.setUser(user);
        this.router.navigate(['/']);
      }, error => {
        this.error = true;
        this.errorMessage = error['error']['non_field_errors'][0];
      }
    );
  }

  ngOnInit() {
    this.storageService.loadUserFromStorage();
    const user = this.storageService.getUser();
    if (user.username !== '') {
      this.router.navigate(['/upload']);
    }
  }
}
