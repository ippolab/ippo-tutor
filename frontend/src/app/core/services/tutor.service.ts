import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable ,  BehaviorSubject ,  ReplaySubject } from 'rxjs';

import { ApiService } from './api.service';
import { User, Tutor } from '../models';
import { map ,  distinctUntilChanged } from 'rxjs/operators';
import { pipe } from '@angular/core/src/render3/pipe';


@Injectable()
export class TutorService {
  private currentTutorSubject = new BehaviorSubject<Tutor>({} as Tutor);
  public currentTutor = this.currentTutorSubject.asObservable().pipe(distinctUntilChanged());

  constructor (
    private apiService: ApiService,
    private http: HttpClient,
  ) {}

  changeInfo(credentials) {
      this.currentTutor.subscribe(
          (tutor) => {
              this.apiService.post(`/tutors/${tutor.username}/`, credentials)
          }
      )
  }

  getCurrentTutor(): Tutor {
      return this.currentTutorSubject.value;
  }
}
