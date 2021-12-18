import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreateStudentComponent } from '../student/create-student/create-student.component';
import { CreateTeacherComponent } from '../teacher/create-teacher/create-teacher.component';

const routes: Routes = [
    {
        path: "teacher",
        component: CreateTeacherComponent
    },
    {
        path: "student",
        component: CreateStudentComponent
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class RegistrationRoutingModule { }
