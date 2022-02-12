using System;
using System.Threading.Tasks;
using Controller;
using DataStore;
using MassTransit;
using Models;

namespace EventConsumer
{
    public class CreateEventConsumer : IConsumer<CreateTeacherModel>
    {
        // TeachersController _TeachersController;
        DataStoreInterface DataStoreInterface;
        public CreateEventConsumer(
            // TeachersController TeachersController
        DataStoreInterface DataStoreInterface)
        {
            // this._TeachersController = TeachersController;
            this.DataStoreInterface = DataStoreInterface;
        }

        public async Task Consume(ConsumeContext<CreateTeacherModel> context)
        {
            Console.WriteLine("HaHa");
            var data = context.Message;
            CreateTeacherModel TeacherModel = new CreateTeacherModel{
                Name = data.Name,
                AboutMe = data.AboutMe,
                DepartmentName = data.DepartmentName,
                OrganizationName = data.OrganizationName
            };
            createTeacher(TeacherModel);
            // _TeachersController.createTeacher(TeacherModel);
        }

        public Guid createTeacher(CreateTeacherModel createTeacherModel)
        {
            Console.WriteLine("HiHi");
            Teacher teacher = new(){
                Id = Guid.NewGuid(),
                Name = createTeacherModel.Name,
                OrganizationName = createTeacherModel.OrganizationName,
                Department = createTeacherModel.DepartmentName,
                AboutMe = createTeacherModel.AboutMe
            };
            DataStoreInterface.createTeacher(teacher);

            return teacher.Id;
        }
    }
}