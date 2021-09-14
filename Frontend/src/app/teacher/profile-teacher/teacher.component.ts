import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
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
    private _teacherService: TeacherService,
    private _activatedRoute: ActivatedRoute
  ) { }
  
  async ngOnInit(): Promise<void> {
    let teacherId = this._activatedRoute.snapshot.queryParams.teacherId;
    let resp = await this._teacherService.getTeacher(teacherId).toPromise();
    this.teacherInfo = resp && resp[0] && new Teacher(resp[0]) || null;
  }

}
