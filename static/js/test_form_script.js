/**
 * test_form_script.js
 *
 * Handles:
 *  1. Image preview when user selects a file.
 *  2. Client-side validation before sending the request.
 *  3. Submitting form data via fetch() as multipart/form-data.
 *  4. Displaying server validation errors inline.
 *  5. Redirecting to /test/success/ on success.
 */

// ── Helper: get CSRF token from the cookie Django sets ──────────
function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === name) return decodeURIComponent(value);
  }
  return null;
}

// ── Image preview ────────────────────────────────────────────────
document.getElementById('profile_image').addEventListener('change', function () {
  const file = this.files[0];
  const wrap = document.getElementById('previewWrap');
  const img  = document.getElementById('previewImg');

  if (file && file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = (e) => {
      img.src = e.target.result;
      wrap.hidden = false;
    };
    reader.readAsDataURL(file);
  } else {
    wrap.hidden = true;
    img.src = '';
  }
});

// ── Clear a single field's error display ────────────────────────
function clearError(fieldId) {
  const el = document.getElementById(fieldId + 'Err');
  if (el) el.textContent = '';
}

// ── Show a single field's error ──────────────────────────────────
function showError(fieldId, message) {
  const el = document.getElementById(fieldId + 'Err');
  if (el) el.textContent = message;
}

// ── Client-side validation ────────────────────────────────────────
function validateForm(formData) {
  let valid = true;
  const fields = ['name', 'email', 'city', 'message'];

  // Clear all errors first
  fields.forEach(f => clearError(f));
  clearError('image');

  fields.forEach(f => {
    if (!formData.get(f) || !formData.get(f).toString().trim()) {
      showError(f, `${f.charAt(0).toUpperCase() + f.slice(1)} is required.`);
      valid = false;
    }
  });

  const img = formData.get('profile_image');
  if (!img || img.size === 0) {
    showError('image', 'Please select a profile image.');
    valid = false;
  }

  return valid;
}

// ── Form submission via fetch() ───────────────────────────────────
document.getElementById('testForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const form      = e.target;
  const formData  = new FormData(form);

  // Client-side validation
  if (!validateForm(formData)) return;

  // UI: show spinner, disable button
  const btn     = document.getElementById('submitBtn');
  const btnText = document.getElementById('btnText');
  const spinner = document.getElementById('btnSpinner');
  btn.disabled    = true;
  btnText.hidden  = true;
  spinner.hidden  = false;

  // Hide previous error banner
  const banner   = document.getElementById('errorBanner');
  const errList  = document.getElementById('errorList');
  banner.hidden  = true;
  errList.innerHTML = '';

  try {
    const response = await fetch('/test/submit/', {
      method: 'POST',
      headers: {
        // Django requires the CSRF token in the X-CSRFToken header
        'X-CSRFToken': getCookie('csrftoken'),
      },
      // Do NOT set Content-Type manually — browser sets it with the boundary for FormData
      body: formData,
    });

    const data = await response.json();

    if (response.ok && data.status === 'ok') {
      // ✅ Success — redirect to confirmation page
      window.location.href = data.redirect;
    } else {
      // ❌ Server validation errors
      const errors = data.errors || { general: ['Something went wrong. Please try again.'] };

      // Show inline errors for known fields
      const fieldMap = {
        name:          'name',
        email:         'email',
        city:          'city',
        message:       'message',
        profile_image: 'image',
      };

      Object.entries(errors).forEach(([field, msg]) => {
        if (fieldMap[field]) {
          showError(fieldMap[field], Array.isArray(msg) ? msg[0] : msg);
        } else {
          // Unknown field — show in banner
          const li = document.createElement('li');
          li.textContent = `${field}: ${Array.isArray(msg) ? msg[0] : msg}`;
          errList.appendChild(li);
        }
      });

      if (errList.children.length > 0) {
        banner.hidden = false;
        banner.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }

      // Re-enable button
      btn.disabled   = false;
      btnText.hidden = false;
      spinner.hidden = true;
    }
  } catch (networkError) {
    // Network / unexpected error
    errList.innerHTML = '<li>Network error. Check your connection and try again.</li>';
    banner.hidden = false;
    btn.disabled   = false;
    btnText.hidden = false;
    spinner.hidden = true;
  }
});
