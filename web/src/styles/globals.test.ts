import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

const css = readFileSync(resolve(process.cwd(), "src/styles/globals.css"), "utf8");

describe("mobile layout CSS contract", () => {
  it("keeps the 320px ranking in two rows without page-level horizontal overflow", () => {
    const mobileStart = css.indexOf("@media (max-width: 640px)");
    const mobileEnd = css.indexOf("@media (prefers-reduced-motion", mobileStart);
    const mobileRules = css.slice(mobileStart, mobileEnd);

    expect(mobileStart).toBeGreaterThanOrEqual(0);
    expect(mobileRules).toMatch(
      /\.sector-ranking button\s*\{[^}]*grid-template-areas:\s*"rank name score change"\s*"rank lifecycle phase change"/,
    );
    expect(css).toMatch(/\.rotation-page\s*\{[^}]*overflow-x:\s*hidden/);
    expect(css).toMatch(/\.lifecycle-bands\s*\{[^}]*overflow-x:\s*auto/);
  });

  it("keeps native date options legible and the Lifecycle toggle compact", () => {
    expect(css).toMatch(/\.filter-field select option\s*\{[^}]*background:\s*#0c192b[^}]*color:\s*var\(--text\)/);
    expect(css).toMatch(/\.filter-field--checkbox input\[type="checkbox"\]\s*\{[^}]*width:\s*16px[^}]*height:\s*16px/);
  });
  it("styles each trading calendar status independently", () => {
    expect(css).toMatch(/\.trading-calendar__day\[data-date-status="snapshot"\]/);
    expect(css).toMatch(/\.trading-calendar__day\[data-date-status="pending"\]/);
    expect(css).toMatch(/\.trading-calendar__day\[data-date-status="closed"\]/);
  });
  it("positions the trading calendar popover outside the filter layout", () => {
    expect(css).toMatch(/\.trading-calendar-filter\s*\{[^}]*position:\s*relative/);
    expect(css).toMatch(/\.trading-calendar-popover\s*\{[^}]*position:\s*absolute[^}]*z-index:\s*\d+/);
    expect(css).toMatch(/\.trading-calendar-trigger\s*\{/);
  });

  it("reserves a fixed, non-wrapping desktop change column for ranking direction and value", () => {
    expect(css).toMatch(/\.ranking-columns, \.sector-ranking button\s*\{[^}]*grid-template-columns:[^;]*72px/);
    expect(css).toMatch(/\.sector-ranking em\s*\{[^}]*white-space:\s*nowrap/);
  });
});
