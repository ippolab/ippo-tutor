import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { CoreModule } from './core';

import { AppComponent } from './app.component';
import { AuthModule } from './auth/auth.module';
import {
  FooterComponent,
  HeaderComponent,
  SharedModule
}from './shared';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    HeaderComponent,
  ],
  imports: [
    AuthModule,
    BrowserModule,
    CoreModule,
    AppRoutingModule,
    SharedModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 
}
