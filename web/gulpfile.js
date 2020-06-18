const gulp = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const concatCss = require('gulp-concat-css');

gulp.task('livereload', function () {
    const spawn = require('child_process').spawn;
    let args = ['manage.py', 'livereload'];
    let livereload = spawn('python', args, {
        stdio: 'inherit'
    });
    livereload.on('close', function (code) {
        if (code !== 0) {
            console.error('Livereload server exited with error code: ' + code);
        } else {
            console.log('Livereload server exited normally.');
        }
    });
});

gulp.task('django', function () {
    const spawn = require('child_process').spawn;
    let args = ['manage.py', 'runserver', '--settings=impuls.settings.development'];
    let runserver = spawn('python', args, {
        stdio: 'inherit'
    });
    runserver.on('close', function (code) {
        if (code !== 0) {
            console.error('Django server exited with error code: ' + code);
        } else {
            console.log('Django server exited normally.');
        }
    });
});

function compileSass(name, path) {
    return function () {
        return gulp
            .src(path)
            .pipe(sass.sync().on('error', sass.logError))
            .pipe(
                autoprefixer({
                    overrideBrowserslist: ['last 10 versions'],
                    cascade: false
                })
            )
            .pipe(concatCss(name + '.css'))
            .pipe(gulp.dest('staticfiles/build/'));
    };
}

gulp.task('watch', function () {
    gulp.watch('staticfiles/sass/*.sass', compileSass('main', 'staticfiles/sass/*.sass'));
});

gulp.task('default', gulp.parallel('livereload', 'django', 'watch'));
