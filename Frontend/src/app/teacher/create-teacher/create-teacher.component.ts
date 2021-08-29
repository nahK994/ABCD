import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-teacher',
  templateUrl: './create-teacher.component.html',
  styleUrls: ['./create-teacher.component.scss']
})
export class CreateTeacherComponent implements OnInit {

  form: FormGroup;

  constructor(
    private _fb: FormBuilder
  ) {
    this.form = this._fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      orgName: ['', Validators.required],
      aboutMe: ['', Validators.required]
    })
  }

  ngOnInit(): void {
  }

  submit()
  {
    console.log("HaHa ===> ", this.form.value)
  }

}
