import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StudentRoutingModule } from './student-routing.module';
import { MatCardModule } from '@angular/material/card';
import { CreateStudentComponent } from './create-student/create-student.component';
import { ProfileStudentComponent } from './profile-student/student.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';



@NgModule({
  declarations: [
    ProfileStudentComponent,
    CreateStudentComponent
  ],
  imports: [
    CommonModule,
    StudentRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    MatFormFieldModule,
    MatButtonModule,
    MatIconModule,
    MatInputModule,
    MatCardModule
  ]
})
export class StudentModule { }
