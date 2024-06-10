import { Link } from "react-router-dom";

function Login() {
  return (
    <div className="form-container">
      <form className="form-content">
        <p>Вход</p>
        <input type="email" name="" id="" placeholder="E-mail" />
        <div>
          <input type="checkbox" name="" id="use-phone-number" />
          <label htmlFor="use-phone-number">Использовать номер телефона</label>
        </div>
        <input type="password" name="" id="" placeholder="Пароль" />
      </form>
      <div className="buttons">
        <Link to="/registration" className="link">Регистрация</Link>
        <Link to="/main" className="form-cancel" type="button">
          <i class="fas fa-times"></i>
        </Link>
        <button className="form-sumbit" type="submit">
          <i class="fas fa-check"></i>
        </button>
      </div>
    </div>
  );
}

export default Login;
