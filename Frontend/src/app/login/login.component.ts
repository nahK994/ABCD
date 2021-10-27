import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { LoginService } from './login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  form: FormGroup;

  constructor(
    private _fb: FormBuilder,
    private _router: Router,
    private _activatedRoute: ActivatedRoute,
    private _loginService: LoginService
  ) {
    this.form = this._fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required]]
    })
  }

  ngOnInit(): void {

  }

  async submit()
  {
    let resp = await this._loginService.loginUser(this.form.value);
    let teacherIdQueryParam = {
      "teacherId": resp
    }
    this._router.navigate(['../teacher/profile'], { relativeTo: this._activatedRoute, queryParams: teacherIdQueryParam });
  }

  createNewStudent()
  {
    this._router.navigate(['/student/create'])
  }

  createNewTeacher()
  {
    this._router.navigate(['/teacher/create'])
  }
}
