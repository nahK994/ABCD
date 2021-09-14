import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { TeacherPayload, TeacherService } from '../teacher.service';

@Component({
  selector: 'app-create-teacher',
  templateUrl: './create-teacher.component.html',
  styleUrls: ['./create-teacher.component.scss']
})
export class CreateTeacherComponent implements OnInit {

  form: FormGroup;

  constructor(
    private _fb: FormBuilder,
    private _teacherService: TeacherService,
    private _router: Router,
    private _activatedRoute: ActivatedRoute
  ) {
    this.form = this._fb.group({
      // name: ['', Validators.required],
      userName: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
      // orgName: ['', Validators.required],
      // aboutMe: ['', Validators.required],
    })
  }

  createGuid()  
  {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {  
        var r = Math.random()*16|0, v = c === 'x' ? r : (r&0x3|0x8);  
        return v.toString(16);  
    });  
  }

  ngOnInit(): void {
  }

  async submit()
  {
    let guidId = this.createGuid()
    let res: TeacherPayload = {
      teacherId: guidId,
      email: this.form.controls['email'].value,
      userName: this.form.controls['userName'].value,
      password: this.form.controls['password'].value
    }
    let resp = await this._teacherService.postTeacher(res).toPromise();

    let teacherIdQueryParam = {
      "teacherId": guidId
    }
    this._router.navigate(['../profile'], { relativeTo: this._activatedRoute, queryParams: teacherIdQueryParam });
  }

}
