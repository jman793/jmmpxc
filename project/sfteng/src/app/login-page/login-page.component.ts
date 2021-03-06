import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  constructor(private authService:AuthService,private router:Router) {
   }

  ngOnInit() {
  }

  googleLogin(){
    this.authService.loginWithGoogle()
  }

  guest(){
    this.router.navigate(['/page'])
  }

  

}
