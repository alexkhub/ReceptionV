function ProfileForm() {
  return (
    <div className="profile-form-container">
      <form className="profile-form-content">
        <div className="section-title">
          <p>Документы</p>
        </div>
        <div className="profile-section">
          <input type="file" name="" id="profile-docs-passport" />
          <label htmlFor="profile-docs-passport">Паспорт</label>
          <input type="file" name="" id="profile-docs-certificate" />
          <label htmlFor="profile-docs-certificate">Аттестат</label>
          <input type="file" name="" id="profile-docs-snils" />
          <label htmlFor="profile-docs-snils">СНИЛС</label>
          <input type="file" name="" id="profile-docs-photo" />
          <label htmlFor="profile-docs-photo">Фотография</label>
          <input type="file" name="" id="profile-docs-medical-certificate" />
          <label htmlFor="profile-docs-medical-certificate">Мед. справка</label>
          <input type="file" name="" id="profile-docs-other" />
          <label htmlFor="profile-docs-other">Другое</label>
        </div>
        <div className="section-title">
          <p>Уровень образования</p>
        </div>
        <div className="profile-section">
          <select name="educational-level" id="educational-level">
            <option value="">Первый</option>
            <option value="">Второй</option>
            <option value="">Три с половиной</option>
          </select>
        </div>
        <div className="section-title">
          <p>Направление</p>
        </div>
        <div className="profile-section">
          <select name="direction" id="direction">
            <option value="">Север</option>
            <option value="">Юг</option>
            <option value="">Запад</option>
            <option value="">Восток</option>
          </select>
        </div>
        <div className="section-title">
          <p>Оценки ОГЭ</p>
        </div>
        <div className="profile-section">
          <div className="scores">
            <div className="score">
              <span className="score__subject-name">Русский язык</span>
              <div className="score-number">
                <p>72</p>
              </div>
            </div>
            <div className="score">
              <span className="score__subject-name">Математика</span>
              <div className="score-number">
                <p>5</p>
              </div>
            </div>
            <div className="score">
              <span className="score__subject-name">Другое</span>
              <div className="score-number">
                <p>142</p>
              </div>
            </div>
            <div className="score">
              <span className="score__subject-name">Средний балл</span>
              <div className="score-number average-score">
                <p>1</p>
              </div>
            </div>
          </div>
        </div>
        <div className="section-title">
          <p>Вопрос</p>
        </div>
        <div className="profile-section">
          <select name="question" id="question">
            <option value="">Как?</option>
            <option value="">Почему?</option>
            <option value="">Ответ</option>
          </select>
        </div>
        <div className="section-title">
          <p>Образовательное учреждение</p>
        </div>
        <div className="profile-section">
          <select name="educational-institution" id="educational-institution">
            <option value="">Хорошее</option>
            <option value="">Ну нормальное</option>
            <option value="">пойдет</option>
          </select>
        </div>
        <button className="form-apply-button" type="submit">
          Подать заявку
        </button>
      </form>
    </div>
  );
}

export default ProfileForm;
