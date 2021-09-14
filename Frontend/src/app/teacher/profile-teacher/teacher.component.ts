import { Component, OnInit } from '@angular/core';
import { Teacher } from '../teacher.model';
import { TeacherService } from '../teacher.service';

@Component({
  selector: 'app-profile-teacher',
  templateUrl: './teacher.component.html',
  styleUrls: ['./teacher.component.scss']
})

export class ProfileTeacherComponent implements OnInit {

  teacherInfo: Teacher;
  constructor(
    private _teacherService: TeacherService
  ) { }
  
  ngOnInit(): void {
    this._teacherService.getTeacher("16").subscribe(resp => {
      this.teacherInfo = resp && resp[0] && new Teacher(resp[0]) || null;
    })
  }

}
