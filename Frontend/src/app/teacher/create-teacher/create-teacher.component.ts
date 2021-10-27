import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { LoginResponse, LoginService } from 'src/app/login/login.service';
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
    private _activatedRoute: ActivatedRoute,
    private _logInService: LoginService
  ) {
    this.form = this._fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      orgName: ['', Validators.required],
      aboutMe: ['', Validators.required],
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
      userId: guidId,
      name: this.form.controls['name'].value,
      orgName: this.form.controls['orgName'].value,
      email: this.form.controls['email'].value,
      aboutMe: this.form.controls['aboutMe'].value,
      password: this.form.controls['password'].value
    }
    let resp: LoginResponse = await this._teacherService.createTeacher(res).toPromise();
    this._logInService.setAssets(resp.refreshToken, resp.accessToken, resp.userId);

    let teacherIdQueryParam = {
      "teacherId": resp.userId
    }
    this._router.navigate(['../profile'], { relativeTo: this._activatedRoute, queryParams: teacherIdQueryParam });
  }

}
