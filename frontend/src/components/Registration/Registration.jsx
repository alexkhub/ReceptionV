import { Link } from "react-router-dom";

function Registration() {
  return (
    <div className="form-container">
      <form className="form-content">
        <p>Регистрация</p>
        <input type="text" name="" id="" placeholder="Имя" />
        <input type="text" name="" id="" placeholder="Фамилия" />
        <input type="text" name="" id="" placeholder="Отчество" />
        <input type="email" name="" id="" placeholder="E-mail" />
        <div>
          <input type="checkbox" name="" id="use-phone-number" />
          <label htmlFor="use-phone-number">Использовать номер телефона</label>
        </div>
        <input type="password" name="" id="" placeholder="Пароль" />
        <input type="password" name="" id="" placeholder="Повторите пароль" />
      </form>
      <div className="buttons">
        <Link to="/login" className="link">
          Войти
        </Link>
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

export default Registration;
