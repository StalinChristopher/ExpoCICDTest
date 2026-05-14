# Expo RN template

Expo SDK app aligned with the Code & Theory React Native template (navigation, theme, TanStack Query, i18n, MMKV).

## CI (GitHub Actions)

When this repo uses the shared `rn.yml` workflow from **template-pipeline-react-native**, the JS gate jobs run:

- `npm run lint` — ESLint (`expo lint`)
- `npm run format:check` — Prettier on `src/**`, `App.tsx`, `index.ts`
- `npm run typecheck` — `tsc --noEmit`
- `npm run test:ci` — Jest with coverage (threshold matches bare template)

Use `npm run format` to fix Prettier issues locally. Install dependencies with **`npm ci`** in CI (this template ships **`package-lock.json`** only).

**Prebuild / committed `android/`:** If you add bare-style native config (for example `react-native-config` with resource shrinking), mirror the bare template’s `res/raw/keep.xml` pattern for generated string resources. The default Expo env path uses `expo-constants` and does not require that for managed workflows.

## Local development

```sh
npm install
npm start
```

See [Expo documentation](https://docs.expo.dev/) for environment setup, `expo prebuild`, and EAS builds.
