import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { routing, appRoutingProviders } from './app.routing';

import { AppComponent } from './app.component';

import { HomeComponent } from './components/home.component';
import { UserEditComponent } from './components/user-edit.component';
import { UserEditPasswordComponent } from './components/user-edit-password.component';
import { ProyectosComponent } from './components/proyectos-list.component';
import { ProyectoCreateComponent } from './components/create-project.component';
import { ProyectoDetallesComponent } from './components/detalles-proyecto.component';
import { MiembroAddComponent } from './components/add-miembro.component'; 
import { RegistrarMiembroComponent } from './components/registrar-miembro.component';
import { ProjectUpdateComponent } from './components/proyecto-update.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    UserEditComponent,
    UserEditPasswordComponent,
    ProyectosComponent,
    ProyectoCreateComponent,
    ProyectoDetallesComponent,
    MiembroAddComponent,
    RegistrarMiembroComponent,
    ProjectUpdateComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    routing
  ],
  providers: [appRoutingProviders],
  bootstrap: [AppComponent]
})
export class AppModule { }