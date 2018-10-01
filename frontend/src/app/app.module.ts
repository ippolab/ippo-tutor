import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { AuthComponent } from './auth/auth.component';
import { StudentUploadComponent } from './student-upload/student-upload.component';

import { AppRoutingModule } from './app-routing.module';
import { UserStorerService } from './user-storer.service';
import { HttpclientService } from './httpclient.service';


@NgModule({
  declarations: [
    AppComponent,
    AuthComponent,
    StudentUploadComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [UserStorerService, HttpclientService],
  bootstrap: [AppComponent]
})
export class AppModule { }
