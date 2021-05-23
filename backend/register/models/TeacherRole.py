from django.db import models


class TeacherRole(models.Model):
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')
    physical_face = models.ForeignKey('PhysicalFace',
                                      on_delete=models.SET_NULL,
                                      related_name='teacher_roles',
                                      blank=True,
                                      null=True,
                                      verbose_name='Физическое лицо')
    academic_rank = models.ForeignKey('AcademicRank',
                                      on_delete=models.SET_NULL,
                                      related_name='teacher_roles',
                                      blank=True,
                                      null=True,
                                      verbose_name='Ученое звание')
    academic_degree = models.ForeignKey('AcademicDegree',
                                        on_delete=models.SET_NULL,
                                        related_name='teacher_roles',
                                        blank=True,
                                        null=True,
                                        verbose_name='Ученая степень')
    qualification_category = models.ForeignKey('QualificationCategory',
                                               on_delete=models.SET_NULL,
                                               related_name='teacher_roles',
                                               blank=True,
                                               null=True,
                                               verbose_name='Квалификационная категория')
    job_position = models.ForeignKey('JobPosition',
                                     on_delete=models.SET_NULL,
                                     related_name='teacher_roles',
                                     blank=True,
                                     null=True,
                                     verbose_name='Должность')
    educational_organization = models.ForeignKey('EducationalOrganization',
                                                 on_delete=models.SET_NULL,
                                                 related_name='teacher_roles',
                                                 blank=True,
                                                 null=True,
                                                 verbose_name='Образовательная организация')

    class Meta:
        verbose_name = 'Роль педагог'
        verbose_name_plural = 'Роли педагогов'
        ordering = ['date_start']

    def __str__(self):
        return self.date_start.strftime('%d %m %Y')
