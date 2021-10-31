import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TeacherRoutingModule } from './teacher-routing.module';
import { MatCardModule } from '@angular/material/card';
import { CreateTeacherComponent } from './create-teacher/create-teacher.component';
import { ProfileTeacherComponent } from './profile-teacher/teacher.component';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TeacherService } from './teacher.service';
import { HttpClientModule } from '@angular/common/http';
import { AppService } from '../app.service';
import { LoginService } from '../login/login.service';


@NgModule({
  declarations: [
    ProfileTeacherComponent,
    CreateTeacherComponent
  ],
  imports: [
    CommonModule,
    TeacherRoutingModule,
    MatCardModule,
    ReactiveFormsModule,
    FormsModule,
    MatFormFieldModule,
    MatButtonModule,
    MatIconModule,
    MatInputModule,
    HttpClientModule
  ],
  providers: [
    TeacherService,
    AppService,
    LoginService
  ]
})
export class TeacherModule { }
