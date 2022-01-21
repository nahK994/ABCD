using System;
using Models;
using System.Collections.Generic;

namespace DataStore
{
    public interface DataStoreInterface
    {
        Student getStudent(Guid Id);
        List<Student> getStudents();
        Guid createStudent(Student Student);
        void updateStudent(Student Student);
        void deleteStudent(Student Student);
    }
}