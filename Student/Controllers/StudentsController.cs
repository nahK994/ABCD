using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using Models;
using DataStore;

namespace Controller
{
    [ApiController]
    [Route("user")]
    public class StudentsController: ControllerBase
    {
        DataStoreInterface DataStoreInterface;
        public StudentsController(DataStoreInterface DataStoreInterface)
        {
            this.DataStoreInterface = DataStoreInterface;
        }

        [HttpGet("/get")]
        public List<Student> getStudents()
        {
            return DataStoreInterface.getStudents();
        }

        [HttpGet("/get/{Id}")]
        public ActionResult<Student> getStudent(Guid Id)
        {
            Student Student = DataStoreInterface.getStudent(Id);
            if(Student is null)
            {
                NotFound();
            }

            return Ok(Student);
        }

        [HttpPut("/put/{Id}")]
        public ActionResult updateUser(UpdateStudentModel updateStudentModel, Guid Id)
        {
            Student Student = DataStoreInterface.getStudent(Id);
            if(Student is null)
            {
                return NotFound();
            }

            Student updatedStudent = Student with {
                OrgName = updateStudentModel.OrgName,
                DeptName = updateStudentModel.DeptName,
                AboutMe = updateStudentModel.AboutMe
            };
            DataStoreInterface.updateStudent(updatedStudent);

            return NoContent();
        }

        [HttpPost("/create")]
        public Guid createUser(CreateStudentModel createStudentModel)
        {
            Student Student = new(){
                Id = Guid.NewGuid(),
                OrgName = createStudentModel.OrgName,
                DeptName = createStudentModel.DeptName,
                AboutMe = createStudentModel.AboutMe
            };

            DataStoreInterface.createStudent(Student);

            return Student.Id;
        }

        [HttpDelete("/delete/{Id}")]
        public ActionResult deleteUser(Guid Id)
        {
            Student user = DataStoreInterface.getStudent(Id);
            if(user is null)
            {
                return NotFound();
            }

            DataStoreInterface.deleteStudent(user);
            return NoContent();
        }
    }
}