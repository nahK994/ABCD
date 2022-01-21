using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using Models;
using DataStore;

namespace Controller
{
    [ApiController]
    [Route("user")]
    public class TeachersController: ControllerBase
    {
        DataStoreInterface DataStoreInterface;
        public TeachersController(DataStoreInterface DataStoreInterface)
        {
            this.DataStoreInterface = DataStoreInterface;
        }

        [HttpGet("/get")]
        public List<Teacher> getTeachers()
        {
            return DataStoreInterface.getTeachers();
        }

        [HttpGet("/get/{Id}")]
        public ActionResult<Teacher> getTeacher(Guid Id)
        {
            Teacher Teacher = DataStoreInterface.getTeacher(Id);
            if(Teacher is null)
            {
                NotFound();
            }

            return Ok(Teacher);
        }

        [HttpPut("/put/{Id}")]
        public ActionResult updateUser(UpdateTeacherModel updateTeacherModel, Guid Id)
        {
            Teacher teacher = DataStoreInterface.getTeacher(Id);
            if(teacher is null)
            {
                return NotFound();
            }

            Teacher updatedTeacher = teacher with {
                OrgName = updateTeacherModel.OrgName,
                DeptName = updateTeacherModel.DeptName,
                AboutMe = updateTeacherModel.AboutMe
            };
            DataStoreInterface.updateTeacher(updatedTeacher);

            return NoContent();
        }

        [HttpPost("/create")]
        public Guid createUser(CreateTeacherModel createTeacherModel)
        {
            Teacher teacher = new(){
                Id = Guid.NewGuid(),
                OrgName = createTeacherModel.OrgName,
                DeptName = createTeacherModel.DeptName,
                AboutMe = createTeacherModel.AboutMe
            };

            DataStoreInterface.createTeacher(teacher);

            return teacher.Id;
        }

        [HttpDelete("/delete/{Id}")]
        public ActionResult deleteUser(Guid Id)
        {
            Teacher user = DataStoreInterface.getTeacher(Id);
            if(user is null)
            {
                return NotFound();
            }

            DataStoreInterface.deleteTeacher(user);
            return NoContent();
        }
    }
}