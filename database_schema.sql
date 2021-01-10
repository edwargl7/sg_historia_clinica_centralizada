CREATE TABLE IF NOT EXISTS public.user_types (
id serial primary key,
name VARCHAR(50) UNIQUE NOT null,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);


CREATE TABLE IF NOT EXISTS public.users (
id serial primary key,
identification_number VARCHAR(20) UNIQUE NOT null,
email VARCHAR(255) NOT NULL,
phone_number VARCHAR(13),
username_type_id bigint not null,
user_type_id bigint not null,
registration_confirmed boolean default false,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
foreign key (username_type_id) references public.user_types (id)
);

CREATE TABLE IF NOT EXISTS public.medical_services (
id serial primary key,
name VARCHAR(255) UNIQUE NOT null,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.hospitals (
id serial primary key,
name VARCHAR(255) UNIQUE NOT null,
address VARCHAR(255) UNIQUE NOT null,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.medical_services_hospitals (
id serial primary key,
hospital_id bigint not null,
medical_service_id bigint not null,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
foreign key (hospital_id) references public.hospitals (id),
foreign key (medical_service_id) references public.medical_services (id)
);

CREATE TABLE IF NOT EXISTS public.patients (
id serial primary key,
name VARCHAR(200) UNIQUE NOT null,
address VARCHAR(255) UNIQUE NOT null,
birth_date date,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.doctors (
id serial primary key,
name VARCHAR(200) UNIQUE NOT null,
address VARCHAR(255) UNIQUE NOT null,
birth_date date,
first_login boolean,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.health_states (
id serial primary key,
name VARCHAR(200) UNIQUE NOT null,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS public.medical_observations (
id serial primary key,
observation VARCHAR(255),
health_state_id bigint not null,
patient_id bigint not null,
doctor_id bigint not null,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
foreign key (health_state_id) references public.health_states (id),
foreign key (patient_id) references public.patients (id),
foreign key (doctor_id) references public.doctors (id)
);




