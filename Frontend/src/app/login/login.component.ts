import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  form: FormGroup;

  constructor(
    private _fb: FormBuilder,
    private route: Router
  ) {
    this.form = this._fb.group({
      userName: ['', Validators.required],
      password: ['', [Validators.required]],
      userType: ['', Validators.required]
    })
  }

  ngOnInit(): void {

  }

  submit()
  {
    console.log("HaHa ===> ", this.form.value)
  }

  createNewStudent()
  {
    this.route.navigate(['/student/create'])
  }

  createNewTeacher()
  {
    this.route.navigate(['/teacher/create'])
  }
}
