import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import { LoginRoutingModule } from './login-routing.module';
import {MatCardModule} from '@angular/material/card';
import {MatSelectModule} from '@angular/material/select';
import { LoginService } from './login.service';
import { HttpClientModule } from '@angular/common/http';
import { AppService } from '../app.service';
import { SelectRoleComponent } from './select-role/select-role.component';


@NgModule({
  declarations: [
    LoginComponent,
    SelectRoleComponent
  ],
  imports: [
    CommonModule,
    LoginRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    MatFormFieldModule,
    MatButtonModule,
    MatIconModule,
    MatInputModule,
    MatCardModule,
    MatSelectModule,
    HttpClientModule
  ],
  providers: [
    LoginService,
    AppService
  ]
})
export class LoginModule { }
