
'use strict';

const DB = {
  KEYS:{ USERS:'ph_users', BOOKINGS:'ph_bookings', SESSION:'ph_session' },
  _get(k){ return JSON.parse(localStorage.getItem(k)||'null'); },
  _set(k,v){ localStorage.setItem(k,JSON.stringify(v)); },

  /* ── Users ── */
  getUsers()     { return this._get(this.KEYS.USERS)||[]; },
  saveUsers(u)   { this._set(this.KEYS.USERS,u); },
  byEmail(email) { return this.getUsers().find(u=>u.email===email.trim().toLowerCase())||null; },

  registerUser({name,email,password,phone=''}){
    if(!name||!email||!password) return{success:false,error:'All fields are required.'};
    if(password.length<6)        return{success:false,error:'Password must be at least 6 characters.'};
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return{success:false,error:'Please enter a valid email address.'};
    if(this.byEmail(email))      return{success:false,error:'An account with this email already exists.'};
    const user={id:'U'+Date.now(),name:name.trim(),email:email.trim().toLowerCase(),password,phone:phone.trim(),createdAt:new Date().toISOString()};
    const list=this.getUsers(); list.push(user); this.saveUsers(list);
    return{success:true,user};
  },

  loginUser({email,password}){
    const u=this.byEmail(email);
    if(!u)               return{success:false,error:'No account found with this email.'};
    if(u.password!==password) return{success:false,error:'Incorrect password. Please try again.'};
    return{success:true,user:u};
  },

  /* ── Session ── */
  getSession()  { return this._get(this.KEYS.SESSION); },
  saveSession(u){ this._set(this.KEYS.SESSION,{id:u.id,name:u.name,email:u.email,phone:u.phone||''}); },
  clearSession(){ localStorage.removeItem(this.KEYS.SESSION); },
  isLoggedIn()  { return this.getSession()!==null; },

  /* ── Bookings ── */
  getBookings()     { return this._get(this.KEYS.BOOKINGS)||[]; },
  saveBookings(b)   { this._set(this.KEYS.BOOKINGS,b); },
  getByUser(email)  { return this.getBookings().filter(b=>b.guestEmail===email.trim().toLowerCase()); },

  createBooking({roomId,guestName,guestEmail,checkin,checkout,guests,special=''}){
    const room=ROOMS.find(r=>r.id===roomId);
    if(!room) return{success:false,error:'Room not found.'};
    const ci=new Date(checkin),co=new Date(checkout);
    if(isNaN(ci)||isNaN(co)) return{success:false,error:'Invalid dates.'};
    if(co<=ci)               return{success:false,error:'Check-out must be after check-in.'};
    const nights=Math.round((co-ci)/86400000);
    const booking={
      id:'BK'+Date.now(), roomId:room.id, roomName:room.name, roomType:room.type,
      roomImg:room.img, roomPrice:room.price, guestName:guestName.trim(),
      guestEmail:guestEmail.trim().toLowerCase(), checkin, checkout, nights,
      guests, special:special.trim(), total:nights*room.price,
      status:'Confirmed', createdAt:new Date().toISOString(),
    };
    const all=this.getBookings(); all.push(booking); this.saveBookings(all);
    return{success:true,booking};
  },

  cancelBooking(id){
    this.saveBookings(this.getBookings().map(b=>b.id===id?{...b,status:'Cancelled'}:b));
  },
};
