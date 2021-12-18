import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
    path: "",
    redirectTo: "/login",
    pathMatch: 'full'
  },
  {
    path: "login",
    loadChildren: () => import('./login/login.module').then(m => m.LoginModule)
  },
  {
    path: "teacher",
    loadChildren: () => import('./teacher/teacher.module').then(m => m.TeacherModule)
  },
  {
    path: "student",
    loadChildren: () => import('./student/student.module').then(m => m.StudentModule)
  },
  {
    path: "profile",
    loadChildren: () => import('./profile/profile.module').then(m => m.ProfileModule)
  },
  {
    path: "create",
    loadChildren: () => import('./registration/registration.module').then(m => m.RegistrationModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
