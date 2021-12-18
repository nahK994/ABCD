import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserInfoComponent } from './user-info/user-info.component';
import { RegistrationRoutingModule } from './registration-routing.module';
import { CreateTeacherComponent } from './create-teacher/create-teacher.component';
import { CreateStudentComponent } from './create-student/create-student.component';



@NgModule({
  declarations: [
    UserInfoComponent,
    CreateTeacherComponent,
    CreateStudentComponent,
  ],
  imports: [
    CommonModule,
    RegistrationRoutingModule
  ]
})
export class RegistrationModule { }
