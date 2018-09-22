import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponent } from './auth/auth.component';
import { StudentUploadComponent } from './student-upload/student-upload.component';

const routes: Routes = [
  { path: 'auth', component: AuthComponent },
  { path: 'student', component: StudentUploadComponent },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}