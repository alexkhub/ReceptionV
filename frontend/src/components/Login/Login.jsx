import axios from "axios";
import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { Link } from "react-router-dom";

function Login() {
  const { register, handleSubmit } = useForm({
    defaultValues: {
      username: "",
      password: "",
    },
  });

  useEffect(() => {
    if (localStorage.getItem("JWT") !== null) {
      window.location.href = "/profile";
    }
  });

  const onSubmit = (data) => {
    if (!localStorage.getItem("JWT")) {
      axios
        .post(`http://127.0.0.1:8000/auth/jwt/create/`, data)
        .then((data) => {
          if (data.status === 200) {
            localStorage.setItem("JWT", data.data.access);
            window.location.href = "/profile";
          }
        });
    }
  };

  return (
    <div className="form-container">
      <form className="form-content">
        <p>Вход</p>
        <input
          type="email"
          name=""
          id=""
          placeholder="E-mail"
          {...register("username")}
        />
        <div>
          <input type="checkbox" name="" id="use-phone-number" />
          <label htmlFor="use-phone-number">Использовать номер телефона</label>
        </div>
        <input
          type="password"
          name=""
          id=""
          placeholder="Пароль"
          {...register("password")}
        />
      </form>
      <div className="buttons">
        <Link to="/registration" className="link">
          Регистрация
        </Link>
        <Link to="/main" className="form-cancel" type="button">
          <i className="fas fa-times"></i>
        </Link>
        <button
          className="form-sumbit"
          type="button"
          onClick={handleSubmit(onSubmit)}
        >
          <i className="fas fa-check"></i>
        </button>
      </div>
    </div>
  );
}

export default Login;
