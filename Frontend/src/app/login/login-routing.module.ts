import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login.component';
import { SelectRoleComponent } from './select-role/select-role.component';

const routes: Routes = [
  {
    path: "",
    component: LoginComponent
  },
  {
    path: "select-role",
    component: SelectRoleComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoginRoutingModule { }
