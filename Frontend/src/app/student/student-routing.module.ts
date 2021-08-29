import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreateStudentComponent } from './create-student/create-student.component';
import { ProfileStudentComponent } from './profile-student/student.component';

const routes: Routes = [
  {
    path: "profile",
    component: ProfileStudentComponent
  },
  {
    path: "create",
    component: CreateStudentComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StudentRoutingModule { }
