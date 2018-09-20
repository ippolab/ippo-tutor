import { Component, OnInit } from '@angular/core';


import { User } from '../users';
import {HttpclientService} from '../httpclient.service'
import { Observable } from '../../../node_modules/rxjs';
import { Student } from '../users';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
  providers:[HttpclientService]
})

export class AuthComponent implements OnInit {

  myUser = new User("", "", false);
  myStudent = new Student('win', '', '', '');

  password = '';
  clickMessage = '';

  onClickMe(name : string, password : string) {
    this.clientService.sendAuthForm(name, password).subscribe(data => this.myUser=data);
    if(this.myUser.istutor == false) this.clientService.getStudent().subscribe(data => this.myStudent=data)
    //todo else getTutor
    this.success();
  }

  success(){
    this.clickMessage = this.myStudent.first_name;
  }

  fail(){
    this.clickMessage = 'you are my hlebushek';
  }
    
 

  constructor(private clientService: HttpclientService){}

  ngOnInit() {
  }

}