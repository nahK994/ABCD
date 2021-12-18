import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProfileRoutingModule } from './profile-routing.module';
import { TeacherComponent } from './teacher/teacher.component';
import { StudentComponent } from './student/student.component';


@NgModule({
  declarations: [
    TeacherComponent,
    StudentComponent
  ],
  imports: [
    CommonModule,
    ProfileRoutingModule
  ]
})
export class ProfileModule { }
