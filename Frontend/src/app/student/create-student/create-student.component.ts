import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-student',
  templateUrl: './create-student.component.html',
  styleUrls: ['./create-student.component.scss']
})
export class CreateStudentComponent implements OnInit {

  form: FormGroup;

  constructor(
    private _fb: FormBuilder
  ) {
    this.form = this._fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]]
    })
  }

  ngOnInit(): void {
  }

  submit()
  {
    console.log("HaHa ===> ", this.form.value)
  }

}
