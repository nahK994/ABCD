import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreateTeacherComponent } from './create-teacher/create-teacher.component';
import { ProfileTeacherComponent } from './profile-teacher/teacher.component';



const routes: Routes = [
  {
    path: "profile",
    component: ProfileTeacherComponent
  },
  {
    path: "create",
    component: CreateTeacherComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TeacherRoutingModule { }
